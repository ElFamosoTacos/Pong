import View
import Controller
import Model

model = Model.Model()
controller = Controller.Controller(model)
view = View.View(model, controller)

view.display()