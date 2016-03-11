class Solution(object):

    def isCrossing(self, points, dist):
        currPos = points[-1]
        ptA = points[-3]
        ptB = points[-4]
        # print "isCrossing: ptA = [%i, %i]" %(ptA[0], ptA[1])
        ind1 = 1 if ptA[0] == ptB[0] else 0
        ind2 = (ind1 + 1) % 2
        end1 = min(ptA[ind1], ptB[ind1])
        end2 = max(ptA[ind1], ptB[ind1])
        # print "isCrossing: currPos = [%i, %i]" %(currPos[0], currPos[1])
        # print "isCrossing: end1 = %i, end2 = %i" %(end1, end2)
        if currPos[ind1] > end2 or currPos[ind1] < end1:
            return False

        if len(points) == 4:
            return abs(ptB[ind2] - currPos[ind2]) <= dist
        elif len(points) == 5:
            ptC = points[-5]
            if currPos[ind1] == ptB[ind1]:
                return abs(ptC[ind2] - currPos[ind2]) <= dist
            else:
                return abs(ptB[ind2] - currPos[ind2]) <= dist
        elif len(points) == 6:
            ptC = points[-5]
            ptD = points[-6]
            if abs(ptC[ind2] - ptB[ind2]) > abs(currPos[ind2] - ptB[ind2]):
                # print "isCrossing: currPos within walls."
                points.pop(0)
                points.pop(0)
                return self.isCrossing(points, dist)
            # print "isCrossing: ptC = [%i, %i]" %(ptC[0], ptC[1])
            # print "isCrossing: ptD = [%i, %i]" %(ptD[0], ptD[1])
            if min(ptC[ind1], ptD[ind1]) <= currPos[ind1] <= max(ptC[ind1], ptD[ind1]):
                return abs(ptC[ind2] - currPos[ind2]) <= dist
            else:
                return abs(ptB[ind2] - currPos[ind2]) <= dist

    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        """
        points = [[0, 0]]
        currPos = [0, 0]
        for i in range(len(x)):
            dist = x[i]

            if i % 4 == 0:
                currPos[1] += dist
            elif i % 4 == 1:
                currPos[0] -= dist
            elif i % 4 == 2:
                currPos[1] -= dist
            else:
                currPos[0] += dist
            # print "currPos = [%i, %i]" %(currPos[0], currPos[1])
            if len(points) < 4:
                points.append(currPos[:])
            else:
                if not self.isCrossing(points, dist):

                    if len(points) == 6:
                        points.pop(0)
                    points.append(currPos[:])
                else:
                    return True
        return False