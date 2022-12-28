from comp import Comp
from dns import DnsDb, Record
from net import Network


def non_recursive_query():
    comp = Comp()
    local_db = DnsDb()
    local_db.add_record(Record("narfu.ru", "1.2.3.4"))
    comp.set_dns_db(local_db)
    comp.iface().set_dns_server("10.20.30.40")

    server = Comp()
    server_db = DnsDb()
    server_db.add_record(Record("google.com", "8.8.8.8"))
    server.set_dns_db(server_db)

    net = Network()
    net.add_host(comp, "11.12.13.14")
    net.add_host(server, "10.20.30.40")
    
    # запрос ко всей сети DNS серверов
    ans = comp.resolve("google.com")

    print(ans)


def recursive_query():
    comp = Comp()
    local_db = DnsDb()
    local_db.add_record(Record("narfu.ru", "1.2.3.4"))
    local_db.add_record(Record("narfu1.ru", "2.3.4.5"))
    comp.set_dns_db(local_db)
    comp.iface().set_dns_server("10.20.30.40")

    server = Comp()
    server_db = DnsDb()
    server_db.add_record(Record("google.com", "8.8.8.8"))
    server.set_dns_db(server_db)
    comp.iface().set_dns_server("10.20.30.40")

    net = Network()
    net.add_host(comp, "11.12.13.14")
    net.add_host(server, "10.20.30.40")
    
    # запрос к конкретному серверу DNS серверу
    ans = net.resolve("11.12.13.14", "narfu1.ru")

    print(ans)


if __name__ == "__main__":
    non_recursive_query()
    recursive_query()
