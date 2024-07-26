import statistics as st
import sys

# #______________Complex Loops 1__________________
months: list[str] = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
t_list: list[int] = [];
i: int = 0;
prev_temp: int = None;
while i < 12:
    try:
        temp: int = int(input(f"What was the temperature in {months[i]}? "));

        if temp < -5 or temp > 40:
            print("wrong data");
        elif not temp and prev_temp == 0:
            continue;
        else:
            print("correct data");
            t_list.append(temp);
            prev_temp = temp;
            i += 1;

    except Exception as e:
        print(f"An {e} -- Error -- has occurred, non numerical data.");

print(f"The yearly average temperature was: {st.mean(t_list):.2f}");
print(f"The yearly lowest temperature was: {min(t_list)}, the coldest month was {months[t_list.index(min(t_list))]}");
print(f"The yearly highest temperature was: {max(t_list)}, the hottest month was {months[t_list.index(max(t_list))]}");

#______________Complex Loops 2__________________
countries: list[str] = ["Argentina", "Australia", "Austria", "Belgium", "Brazil", "Canada", "Chile", "China",
                        "Colombia", "Czech Republic", "Denmark", "Egypt", "Finland", "France", "Germany", "Greece",
                        "Hungary", "India", "Indonesia", "Ireland", "Israel", "Italy", "Japan", "Malaysia",
                        "Mexico", "Netherlands", "New Zealand", "Nigeria", "Norway", "Pakistan", "Peru", "Philippines",
                        "Poland", "Portugal", "Russia", "Saudi Arabia", "Singapore", "South Africa", "South Korea",
                        "Spain", "Sweden", "Switzerland", "Turkey", "United States"];
list_1: list[int] =[];
list_2: list[int] =[];
# list_3: list[int] =[];
i: int = 0;
print("    -------UN vote started-------    ");
topic: str = input("what is the topic being voted on? ");
while i < 44:
    try:
        vote: int = int(input(f"What was the vote of {countries[i]}? "));

        match vote:
            case 1:
                list_1.append(i);
                i += 1;
            case 2:
                list_2.append(i);
                i += 1;
            case 3:
                # list_3.append(i);
                i += 1;
            case 4:
                print(f"country number {i + 1}: {countries[i]} cast a VETO");
                # break;
                sys.exit();
            case _:
                print("invalid input");
                continue;

    except Exception as e:
        print(f"An {e} -- Error -- has occurred, non numerical data.");
print(f"{topic}: resolution was approved") if len(list_1) > len(list_2) else print(f"{topic}: resolution was rejected");
if len(list_1):
    print(f"the first country to vote for the decision was: {list_1[0]}.{countries[list_1[0]]}");
else:
    print(f"against vote on {topic} was unanimous");

if len(list_2):
    print(f"the last country to vote against the decision was: {list_2[len(list_2) - 1]}.{countries[list_2[len(list_2) - 1]]}");
else:
    print(f"for vote on {topic} was unanimous");