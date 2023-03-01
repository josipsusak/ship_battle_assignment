from rest_framework.response import Response
from rest_framework.views import APIView
from ship.views import Ship


class Battle(APIView, Ship):

    def get(self, request):
        attention = "Please enter an URL in a suggested numerical format: http://127.0.0.1:8000/?ships=A,B,C..."
        """ Check if URL has /?ships=...., if it doesn't, raise an exception, and return message"""
        try:
            query_parameters = self.request.GET.get("ships", None).split(",")
            print(query_parameters)
            print(type(query_parameters))
            list_of_soldiers = [int(parameter) for parameter in query_parameters]
            ships_list = self.create_ships(list_of_soldiers)
            return Response({"ships_list": ships_list})
        except (AttributeError, ValueError):
            return Response({
                'Attention': attention})

    """ Create ships with stats, based on query parameters"""
    def create_ships(self, soldiers):
        counter = 1
        ships_data = []
        for i in soldiers:
            new_ship = Ship(i)
            name = "Ship" + str(counter)
            counter += 1
            print(name)
            print(new_ship.num_of_soldiers)
            print(new_ship.ship_hp)
            data = dict(name=name,
                        ship_hp=new_ship.ship_hp,
                        number_of_soldiers=new_ship.num_of_soldiers)
            ships_data.append(data)
        return ships_data
