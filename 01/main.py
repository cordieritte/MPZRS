from classes import *

def main():
    # создаине эеземпляров класса
    comp1 = Computer()
    comp2 = Computer()
    
    # добавление и проверка сервисов Files
    comp1.add_service(Files(comp1))
    comp2.add_service(Files(comp2))
    
    comp1.send_request(comp2, "files", "list")
    comp1.send_request(comp2, "files", "add files", "fileABC.txt")  
    comp2.send_request(comp1, "files", "list")
    
    comp2.send_request(comp1, "files", "space")
    comp2.send_request(comp1, "files", "reduce space", 4321)
    comp1.send_request(comp2, "files", "space")
    
    # добавление и проверка сервиса Clock
    comp2.add_service(Clock())
    comp1.send_request(comp2, "clock", "now", "local")
    comp1.send_request(comp2, "clock", "now", "utc")
    comp1.send_request(comp2, "clock", "now", "+3")
    comp1.send_request(comp2, "clock", "date of birth", "Pushkin")
    
    # добавление и проверка сервиса Network
    comp2.add_service(Network())
    comp1.send_request(comp2, "network", "check")
    
    
    
if __name__ == "__main__":
    main()