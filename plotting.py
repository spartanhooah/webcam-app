from capture import df as data
from bokeh.plotting import figure, show, output_file

print(data)
plot = figure(x_axis_type="datetime", height=100, width=500, title="Motion Graph")

glyph = plot.quad(left=data["Start"], right=["End"], bottom=0, top=1, color="green")

output_file("Graph.html")
show(plot)