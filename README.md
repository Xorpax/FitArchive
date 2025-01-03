# workoutTracker

This is my personal workout tracker that uses pandas for data manipulation of the csv collection of my workouts and their respective PRs

By the end the app should:

- allow me to add new workouts and the records
- have a functional GUI
- visualise the target muscles using a diagram
- offer different ways of visualising my progress (bar charts, pie charts, graphs, etc.)

- pyinstaller --windowed --hidden-import=pandas._libs.tslibs.base --hidden-import=PIL --add-data="C:\Users\petar\AppData\Local\Programs\Python\Python313\Lib\site-packages;pillow" --add-data="C:\Users\petar\AppData\Local\Programs\Python\Python313\Lib\site-packages;customtkinter" -n FitArchive .\app.py