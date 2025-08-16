tolerance = 0.0019

application = "Toy"
if tolerance < 0.1 then application = "Commercial" end
if tolerance < 0.01 then application = "Military" end
if tolerance < 0.001 then application = "Space Exploration" end

print(application)