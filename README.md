# signum3
Details and helpful files for the Signum 3 adjustable ergonomic mechanical keyboard

![alt text](https://i.imgur.com/TWBpaAk.jpg "Signum 3 prototype pcb build")

## Current design issues
- [ ] Pinky columns too low
- [ ] Supports overall finger column height adjustment, but not really so for individual finger height
- Issue with the 1/3u footprint spacing
- Reduce separation to, around less than 1/6 and confirm movement within the scope of general finger length (IE: Increasing height on pinky column should not raise the column higher than ring finger column)
- [ ] Correct cutting paths
  - Bottom left router edge
  - Upper right arc bulge overtravel

## Future Features?
- [ ] OLED screen
  - LOL
  - Nano controlled
  - Rotary+click dial menu interface
  - Pomodoro display and menu management
  - Screensavers
  - Calculator???
- [ ] Pro Micro support
- [ ] Cover for exposed MCU (AKA: Mt Dew shield)
  - alternate mount location for MCU reset button
- [ ] Number row (optional but supported)
- [ ] Correct silk screen locations
  - Correct triple switch footprint silk screen borders, and make two sided
  - Correct Diode polarity print to not be overlapped by SMD footprint
- [ ] Add M2 (case) mounts on corners
- [ ] USB wire mounts for teensy connector bypass
- [ ] Annoy-otron 5k
  - AKA Pomodoro interrupter
  - Counts down pomodoros
  - Counts UP wasted time on unacknowledged time expirations
  - Beeps with PCB mount speaker
  - Vibrates keyboard with mounted motor?!?!
  - Figure out a way to shut off input so you CAN'T continue working?
- [ ] Mini USB hub (header mounted with paths to optional USB A female ports)
  - Requires wire mount for bypass teensy plug to hub rather than wire mounts
  - Parts are iffy, or board mount full circuit and SMD solder (cost bump)
- [ ] Alternative switch locations (duplicates)
  - Bottom keys 2 and 3 in from the corner keys
  - Map to additional optional 3rd thumb key
  - Map to 3.5mm mono pcb mount jack (footpedal?!)
- [ ] Hinge-ability, Plico style
  - How tho? PCB mount slip ring and brushes?
- [ ] Alternative split angle support
- [ ] Full Split support with QMK and pro micrii?
