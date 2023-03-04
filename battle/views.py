from famine.views import Famine
from rest_framework.response import Response
from rest_framework.views import APIView
from ship.views import Ship
from storm.views import Storm


class Battle(APIView, Ship):

    def get(self, request):
        attention = "Please enter an URL in a suggested numerical format: http://127.0.0.1:8000/?ships=A,B,C..."
        """ Check if URL has /?ships=...., if it doesn't, raise an exception, and return message"""
        try:
            query_parameters = self.request.query_params.get("ships", None).split(",")
            print(query_parameters)
            print(type(query_parameters))
        except (AttributeError, ValueError):
            return Response({'Attention': attention})
        else:
            list_of_soldiers = [abs(int(parameter)) for parameter in query_parameters]
            ships_list = self.create_ships(list_of_soldiers)
            print(ships_list)
            final_result = self.storm_and_famine_hits(ships_list)
            return Response({"Winner is": final_result,
                             "Results of a core": ships_list}
                            )

    def storm_and_famine_hits(self, ships_list):
        for ship in ships_list:
            storm = Storm(ship["ship_hp"], ship["number_of_soldiers"])
            famine = Famine(ship["number_of_soldiers"])
            storm_hits_ship = storm.hit_ship()
            ship.update({"ship_hp": storm_hits_ship})
            storm_hits_soldiers = storm.hit_soldiers()
            ship.update({"number_of_soldiers": storm_hits_soldiers})
            famine_hit_soldiers = famine.hit_soldiers()
            ship.update({"number_of_soldiers": famine_hit_soldiers})
        result = self.calculate_result(ships_list)
        return result

    def calculate_result(self, battle_results):
        score = {}
        for ship in battle_results:
            ship_score = int(ship["ship_hp"] + ship["number_of_soldiers"])
            score[ship["name"]] = ship_score
        result = max(score, key=score.get)
        return result
