## Solution (Will not be included in the final version)
```python
while True:

   value = potentiometer.value

   if current_state is state_off:
      leds.fill((0, 0, 0))
      leds.show()

      changed = False

      if value > 21844:
         current_state = state_smooth

   elif current_state is state_smooth:

      brightness, running, changed = vs.sequence(sequence=smooth_sequence, loop_max=0)  # Loop indefinitely

      if value < 21845:
         current_state = state_off
      elif value > 43960:
         current_state = state_party

   elif current_state is state_party:

      brightness, running, changed = vs.sequence(sequence=flicker_sequence, loop_max=0)  # Loop indefinitely

      if value < 43961:
         current_state = state_smooth

   if changed:
      leds.fill((brightness, brightness, brightness))
      leds.show()
   time.sleep(0.1)  # Small delay to allow updates
```