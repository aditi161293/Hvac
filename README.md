# CleanEnergyHVACGroup

To install needed libraries run `pip install -r requirements.txt`


To run, from this directory run `python gym-hvac/hvac_learner.py path_to/csv_file`

Once the training has finished, checkout `graphing` branch and run `python gym-hvac/plotter.py path_to/csv_file` to simulate and save the days. You will need to change the interval of saving figures to save only the ones you'd like


It takes the model about 300 epochs (days) to make it through the entire day. After that it will tune itself to optimize the temperature


TODO: Finalize the reward function. Right now it is a constant reward when the heater is off. More tuning needs to happen here.

