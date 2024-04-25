from Models.Qa_Engineer_Factory import QaEngineerFactory
from Models.Developer_Engineer_Factory import DeveloperEngineerFactory
from Models.Engineer_Model import Engineer
from Controllers.Controller import Controller
from Views.Engineer_View import Engineer_View
from Models.Task_Model import Task
from Models.DevTask import DevTask
from Models.QaTask import QaTask
from Models.DevTaskAdapter import DevTaskAdapter
from Models.QaTaskAdapter import QaTaskAdapter


if __name__ == "__main__":
    
    controller = Controller()
    viewEngineer = Engineer_View(controller)

    engineer1 = controller.create_qa_engineer("Alice")
    engineer2 = controller.create_dev_engineer("Bob")
    engineer3 = controller.create_qa_engineer("Jose")

    # print(f"QA Engineer: {engineer1.getName()} - {engineer1.getRol()}")
    # print(f"Developer Engineer: {engineer2.getName()} - {engineer2.getRol()}")

    controller.add_qa_engineer(engineer1)
    controller.add_qa_engineer(engineer3)
    controller.add_dev_engineer(engineer2)

    viewEngineer.show_all_qa_engineers()
    viewEngineer.show_all_dev_engineers()

    
    #Crear tarea en desarrollo
    dev_task = controller.create_dev_task("Primer tarea", "3 hrs", "Desarrollo", engineer1)
    
    print(f"Tarea en estado de: {dev_task.state}")
    
    adap_to_qa = controller.adapt_to_qa(dev_task)
    
    print(f"tarea en estado de: {adap_to_qa.state} ")