#Installing Slugs

https://github.com/VerifiableRobotics/slugs.git

There is readme file for how to install.

#To try out the files 
Navigate to the folder "hri_reactive_synthesis." Then run the following commands in the terminal:


```
slugs delivery.slugsin --explicitStrategy --jsonOutput > $slugs_reactive/ctrl.json


slugs_compiler delivery.structuredslugs > delivery.slugsin

```

I have the following shortcuts in my .bashrc to use these commands:
```
alias slugs_compiler="python /home/rachel/reactive_synthesis/slugs/tools/StructuredSlugsParser/compiler.py"
slugs_reactive="/home/rachel/reactive_synthesis/hri_reactive_synthesis"
```

You can then simulate a sample path by running sim_paths.py.

The variable "node_init" allows you to start the simulation from a different initial state. 
