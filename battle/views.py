from rest_framework.response import Response
from rest_framework.views import APIView
from ship.views import Ship
from storm.views import Storm
from famine.views import Famine


class Battle(APIView, Ship, Storm):

    def get(self, request):
        attention = "Please enter an URL in a suggested numerical format: http://127.0.0.1:8000/?ships=A,B,C..."
        """ Check if URL has /?ships=...., if it doesn't, raise an exception, and return message"""
        try:
            query_parameters = self.request.GET.get("ships", None).split(",")
            print(query_parameters)
            print(type(query_parameters))
        except (AttributeError, ValueError):
            return Response({'Attention': attention})
        else:
            list_of_soldiers = [int(parameter) for parameter in query_parameters]
            ships_list = self.create_ships(list_of_soldiers)
            print(ships_list)
            for ship in ships_list:
                storm = Storm(ship["ship_hp"], ship["number_of_soldiers"])
                famine = Famine(ship["number_of_soldiers"])
                storm_hits_ship = storm.hit_ship()
                ship.update({"ship_hp": storm_hits_ship})
                storm_hits_soldiers = storm.hit_soldiers()
                ship.update({"number_of_soldiers": storm_hits_soldiers})
                famine_hit_soldiers = famine.hit_soldiers()
                ship.update({"number_of_soldiers": famine_hit_soldiers})
            return Response({"ships_list": ships_list})


