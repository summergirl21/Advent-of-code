def main():
    with open("PuzzleInput2.txt") as file:
        numCubes = {"red": 12, "green": 13, "blue": 14}
        # print(numCubes)
        total = 0
        for line in file:
            line = line.strip()
            #print(line)
            gameNumString, data = line.split(":")
            numStr = gameNumString.strip("Game")
            gameNum = int(numStr)
            #print(gameNum)
            gameData = data.split(";")
            isPossible = isGamePossible(numCubes, gameData)
            if isPossible:
                total += gameNum
            #print(f"Game {gameNum}: isPossible: {isPossible}\n")
        print(f"Part 1 answer: {total}")

    with open("PuzzleInput2.txt") as file:
        total = 0
        for line in file:
            line = line.strip()
            #print(line)
            gameNumString, data = line.split(":")
            numStr = gameNumString.strip("Game")
            gameNum = int(numStr)
            #print(f"Game number: {gameNum}")
            gameData = data.split(";")
            minSet = findMinSet(gameData)
            power = 1
            for cubeCount in minSet.values():
                power = power * cubeCount
            total += power
            #print(f"Power: {power}\n")
        print(f"Part 2 answer: {total}")


def isGamePossible(numCubes, gameData):
    #print(f"isGamePossible: {gameData}, numCubes: {numCubes}")
    for game in gameData:
        cubeData = game.split(",")
        #print(f"cubeData: {cubeData}")
        for cubeInfo in cubeData:
            cubeInfo = cubeInfo.strip()
            color = findCubeColor(numCubes.keys(), cubeInfo)
            numStr = cubeInfo.strip(color)
            cubeNum = int(numStr)
            #print(f"color: {color}, num: {cubeNum}")
            if cubeNum > numCubes[color]:
                #print(f"Not possible: color: {color}, num: {cubeNum}")
                return False
    return True

def findCubeColor(colors, cubeInfo):
    for color in colors:
        if cubeInfo.find(color) > -1:
            return color


def findMinSet(gameData):
    minCubeSet = {"red": 0, "green": 0, "blue": 0}
    #print(f"GameData: {gameData}")
    for game in gameData:
        cubeData = game.split(",")
        #print(f"cubeData: {cubeData}")
        for cubeInfo in cubeData:
            cubeInfo = cubeInfo.strip()
            color = findCubeColor(minCubeSet.keys(), cubeInfo)
            numStr = cubeInfo.strip(color)
            cubeNum = int(numStr)
            #print(f"color: {color}, num: {cubeNum}")
            if cubeNum > minCubeSet[color]:
                minCubeSet[color] = cubeNum
    #print(f"minCubeSet: {minCubeSet}")
    return minCubeSet

if __name__ == "__main__":
    main()