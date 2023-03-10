from famine.views import Famine
from rest_framework.response import Response
from rest_framework.views import APIView
from ship.views import Ship
from storm.views import Storm


class Battle(APIView):

    def get(self, request):
        attention = "Please enter an URL in a suggested numerical format: http://127.0.0.1:8000/?ships=1,2,3..."
        # Check if URL has /?ships=...., if it doesn't, raise an exception, and return message
        try:
            query_parameters = self.request.query_params.get("ships", None).split(",")
            list_of_soldiers = [abs(int(parameter)) for parameter in query_parameters]
        except (AttributeError, ValueError):
            return Response({'Attention': attention})
        else:
            ships_list = Ship().create_ships(list_of_soldiers)
            final_result = self.storm_and_famine_hits(ships_list)
            return Response({"Winner with the highest ship HP and number of solders is": final_result,
                             "Results of a battle": ships_list}
                            )

    def storm_and_famine_hits(self, ships_list):
        for ship in ships_list:
            self.create_storm(ship)
            self.create_famine(ship)
        result = self.calculate_result(ships_list)
        return result

    def calculate_result(self, battle_results):
        score = {}
        for ship in battle_results:
            ship_score = int(ship["ship_hp"] + ship["number_of_soldiers"])
            score[ship["name"]] = ship_score
        result = max(score, key=score.get)
        return result

    def create_storm(self, ship):
        storm = Storm(ship["ship_hp"], ship["number_of_soldiers"])
        storm_hits_ship = storm.hit_ship()
        ship.update({"ship_hp": storm_hits_ship})
        storm_hits_soldiers = storm.hit_soldiers()
        ship.update({"number_of_soldiers": storm_hits_soldiers})
        return ship

    def create_famine(self, ship):
        famine = Famine(ship["number_of_soldiers"])
        famine_hit_soldiers = famine.hit_soldiers()
        ship.update({"number_of_soldiers": famine_hit_soldiers})
        return ship
