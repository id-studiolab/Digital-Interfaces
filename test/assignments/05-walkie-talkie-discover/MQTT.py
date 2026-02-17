import time
import ssl
import os
import wifi
import socketpool

import adafruit_minimqtt.adafruit_minimqtt as MQTT


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
    _require_env(["CIRCUITPY_WIFI_SSID", "CIRCUITPY_WIFI_PASSWORD"])
    print("Connecting to WiFi...")
    wifi.radio.connect(os.getenv("CIRCUITPY_WIFI_SSID"), os.getenv("CIRCUITPY_WIFI_PASSWORD"))
    print("Connected! IP:", wifi.radio.ipv4_address)


def Create_MQTT(
    client_id,
    message_handler=message,
    connection_handler=connected,
    disconnected_handler=disconnected,
):
    _require_env(["MQTT_BROKER"])
    _connect_wifi()

    pool = socketpool.SocketPool(wifi.radio)

    broker = os.getenv("MQTT_BROKER")
    port = int(os.getenv("MQTT_PORT", "1883"))

    # FIX: use MQTT_USERNAME, not MQTT_CLIENT_ID
    username = os.getenv("MQTT_USERNAME") or None
    password = os.getenv("MQTT_PASSWORD") or None

    use_tls = os.getenv("MQTT_USE_TLS", "false").lower() == "true"

    # Use a realistic default for cloud brokers
    socket_timeout = float(os.getenv("MQTT_SOCKET_TIMEOUT", "0.11"))

    ssl_context = ssl.create_default_context() if use_tls else None

    mqtt_client = MQTT.MQTT(
        client_id=client_id,
        broker=broker,
        port=port,
        username=username,
        password=password,
        socket_pool=pool,
        ssl_context=ssl_context,
        socket_timeout=socket_timeout,
    )

    mqtt_client.on_connect = connection_handler
    mqtt_client.on_disconnect = disconnected_handler
    mqtt_client.on_message = message_handler

    print(f"Connecting to mqtt broker {broker}:{port} (TLS={use_tls})")
    mqtt_client.connect()
    
    #mqtt_client.publish("debug/presence", "online")
    #mqtt_client.subscribe("debug/presence")

    # Return a loop timeout that satisfies MiniMQTT: loop_timeout > socket_timeout
    loop_timeout = max(0.050, socket_timeout + 0.01)
    return mqtt_client, loop_timeout
