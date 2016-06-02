# Overlord
# Author: Blake Sawyer, Robert Berglund, Daniel Schiefer
# 
# Control process distribution, monitor cpu cores, manage queues, run simulation
import Processes
import Algorithms
import cpuScheduler
import Processors

# correct my syntax if it's wrong...
def Overlord():
	# Start GUI
        app = QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QWidget()
        ui = Ui_Form()
        ui.setupUi(Form)
        Form.show()
	
	
	# Return variables from GUI
	


	
        sys.exit(app.exec_())
