class Solution(object):

    def getNextTicket(self, tickets, start):
        result = None
        city = None
        for i, ticket in enumerate(tickets):
            if ticket[0] == start:
                if city is None or ticket[1] < city:
                    city = ticket[1]
                    result = i
        return result

    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        next_city_indices = self.getNextTickets(tickets, "JFK")
        results = []
        for next_city_index in next_city_indices:
            temp_tickets = tickets[:]
            ticket = temp_tickets.pop(next_city_index)
            result = [ticket[1]]
            while temp_tickets:
                current_city = result[-1]
                next_city_index = self.getNextTicket(temp_tickets, current_city)
                if next_city_index is None:
                    results.append(result)
                    break
                else:
                    result.append(temp_tickets[next_city_index][1])
                    temp_tickets.pop(next_city_index)
            results.append(result)
        max_len = max(len(x) for x in results)
        longest = [result for result in results if len(result) == max_len ]
        longest.sort()
        return ["JFK"] + longest[0]
        # return self.findItineraryHelper("JFK", tickets)

    def getNextTickets(self, tickets, start):
        indices = []
        for i, ticket in enumerate(tickets):
            if ticket[0] == start:
                indices.append(i)
        return indices

    def findItineraryHelper(self, current, tickets):
        # print "current = " + current
        # print tickets
        # if not tickets:
        #     return []
        cities = [current]
        if not tickets:
            return cities
        next_city_indices = self.getNextTickets(tickets, current)
        temp_result = []
        for index in next_city_indices:
            next_city = tickets[index][1]
            # print "next_city = " + next_city
            ticket = tickets.pop(index)
            result = self.findItineraryHelper(next_city, tickets)
            # print result
            if result:
                if len(result) > len(temp_result):
                    temp_result = result
                elif len(result) == len(temp_result):
                    if result < temp_result:
                        temp_result = result
            tickets.insert(index, ticket)
        return cities + temp_result
