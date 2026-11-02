package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func main() {
	dial := 50
	zeroCount := 0
	anyCount := 0

	file, err := os.Open("../input/day-01.in")
	if err != nil {
		log.Fatal("error opening file: %s", err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		line := scanner.Text()

		direction := string(line[0])
		lineSteps := line[1:]
		steps, err := strconv.Atoi(lineSteps)
		if err != nil {
			log.Fatal("error converting num: %s", err)
		}

		// count extra rotations then cut them from total
		anyCount += steps / 100
		steps %= 100

		if direction == "L" {
			steps *= -1
		}

		//fmt.Printf("%d => %d\n", dial, (dial+steps+100)%100)

		nextDial := dial + steps

		// count going across zero (except when starting on zero)
		if dial != 0 && (nextDial <= 0 || nextDial >= 100) {
			anyCount += 1
		}

		nextDial = (nextDial + 100) % 100

		// count landing exactly on zero
		if nextDial == 0 {
			zeroCount += 1
		}

		dial = nextDial
	}

	if err := scanner.Err(); err != nil {
		log.Fatal("error scanning: %s", err)
	}

	fmt.Printf("Part 1: %d\n", zeroCount)
	fmt.Printf("Part 2: %d\n", anyCount)
}
