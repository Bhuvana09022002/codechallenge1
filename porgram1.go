package main

import (
	"fmt"
	"strconv"
)

func main() {
	// the vendor,item,cost,time are given here:
	var vendors = []string{"V1", "V2", "V1", "V1", "V3", "V3", "V4", "V5"}
	var items = []string{"Banana", "Banana", "Broccoli", "Apple", "Apple", "Orange", "Tomato", "Banana"}
	var Cost_Per_KG = []int{200, 190, 160, 500, 200, 20, 20, 190}
	var Time_to_Deliver = []int{120, 60, 120, 120, 120, 30, 60, 30}

	// to get the user input variables are declared here
	var Purchase_id string
	var item string
	var required_quantity int
	// scanning the input
	fmt.Print("Enter purchase id, item, and required quantity\n")
	fmt.Scanln(&Purchase_id)
	fmt.Scanln(&item)
	fmt.Scanln(&required_quantity)

	var final []string
	final = append(final, Purchase_id, item, strconv.Itoa(required_quantity))
	//to check wheather the input is present int list or not
	var minimum int = 1000
	var time int = 300
	var position int
	for i := 0; i < len(vendors); i++ {
		if item == items[i] {
			final = append(final, "TRUE")
			break
		} else {
			final = append(final, "FALSE", " ")
			break
		}
	}
	for i := 0; i < len(vendors); i++ {
		if item == items[i] {
			if minimum == Cost_Per_KG[i] {
				if time > Time_to_Deliver[i] {
					minimum = Cost_Per_KG[i]
					time = Time_to_Deliver[i]
					position = i
				}
			} else if minimum > Cost_Per_KG[i] {
				minimum = Cost_Per_KG[i]
				time = Time_to_Deliver[i]
				position = i
			}
		}
	}
	if item == items[position] {
		var Total int = minimum * required_quantity
		final = append(final, strconv.Itoa(Total), vendors[position])
		//The final output
		fmt.Println(final)
	} else {
		final = append(final, "0", "0")
		fmt.Println(final)
	}

}
