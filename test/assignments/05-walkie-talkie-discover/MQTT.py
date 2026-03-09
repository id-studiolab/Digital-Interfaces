import time
import os
import adafruit_minimqtt.adafruit_minimqtt as MQTT

# --- DYNAMIC HARDWARE DETECTION ---
try:
    import wifi
    import socketpool
    import ssl
    HAS_NATIVE_WIFI = True
except ImportError:
    # We are on the ItsyBitsy M4 (or similar) without native WiFi/SSL
    HAS_NATIVE_WIFI = False
    import board
    import busio
    from digitalio import DigitalInOut
    from adafruit_esp32spi import adafruit_esp32spi
    import adafruit_esp32spi.adafruit_esp32spi_socket as esp32spi_socket

# Global for the ESP32 interface if using the SPI co-processor
esp32_interface = None


def connected(client, userdata, flags, rc):
    print("Connected to the mqtt broker.")

def disconnected(client, userdata, rc):
    print("Disconnected from the mqtt broker.")

def message(client, topic, m):
    print("New message on topic {0}: {1}".format(topic, m))

def _require_env(keys):
    missing = [k for k in keys if os.getenv(k) is None]
    if missing:
        raise RuntimeError("settings.toml is missing required keys: " + ", ".join(missing))


def _connect_wifi():
    global esp32_interface
    _require_env(["CIRCUITPY_WIFI_SSID", "CIRCUITPY_WIFI_PASSWORD"])
    ssid = os.getenv("CIRCUITPY_WIFI_SSID")
    password = os.getenv("CIRCUITPY_WIFI_PASSWORD")
    print("Connecting to WiFi...")

    if HAS_NATIVE_WIFI:
        # --- PICO 2 W SETUP ---
        wifi.radio.connect(ssid, password)
        print("Connected! IP:", wifi.radio.ipv4_address)
    else:
        # --- ITSYBITSY M4 + ESP32 SPI SETUP ---
        # IMPORTANT: Update these pins to match your actual physical wiring!
        spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
        esp32_cs = DigitalInOut(board.D9)
        esp32_ready = DigitalInOut(board.D11)
        esp32_reset = DigitalInOut(board.D12)

        esp32_interface = adafruit_esp32spi.ESP_SPIcontrol(spi, esp32_cs, esp32_ready, esp32_reset)

        while not esp32_interface.is_connected:
            try:
                esp32_interface.connect_AP(ssid, password)
            except RuntimeError as e:
                print("Could not connect to AP, retrying: ", e)
                continue
        print("Connected! IP:", esp32_interface.pretty_ip(esp32_interface.ip_address))


def Create_MQTT(
    client_id,
    message_handler=message,
    connection_handler=connected,
    disconnected_handler=disconnected,
):
    _require_env(["MQTT_BROKER"])
    _connect_wifi()

    broker = os.getenv("MQTT_BROKER")
    port = int(os.getenv("MQTT_PORT", "1883"))
    username = os.getenv("MQTT_USERNAME") or None
    password = os.getenv("MQTT_PASSWORD") or None
    use_tls = os.getenv("MQTT_USE_TLS", "false").lower() == "true"
    socket_timeout = float(os.getenv("MQTT_SOCKET_TIMEOUT", "0.11"))

    # --- DYNAMIC SOCKET AND SSL SETUP ---
    if HAS_NATIVE_WIFI:
        pool = socketpool.SocketPool(wifi.radio)
        ssl_context = ssl.create_default_context() if use_tls else None
        is_ssl = False # Native networking relies on ssl_context
    else:
        esp32spi_socket.set_interface(esp32_interface)
        pool = esp32spi_socket
        ssl_context = None # ESP32 handles TLS internally, no context needed
        is_ssl = use_tls   # Tell MiniMQTT to instruct the ESP32 to use TLS

    mqtt_client = MQTT.MQTT(
        client_id=client_id,
        broker=broker,
        port=port,
        username=username,
        password=password,
        socket_pool=pool,
        ssl_context=ssl_context,
        is_ssl=is_ssl,     # Required for ESP32 SPI co-processors
        socket_timeout=socket_timeout,
    )

    mqtt_client.on_connect = connection_handler
    mqtt_client.on_disconnect = disconnected_handler
    mqtt_client.on_message = message_handler

    print(f"Connecting to mqtt broker {broker}:{port} (TLS={use_tls})")
    mqtt_client.connect()

    # Return a loop timeout that satisfies MiniMQTT: loop_timeout > socket_timeout
    loop_timeout = max(0.050, socket_timeout + 0.01)
    return mqtt_client, loop_timeout