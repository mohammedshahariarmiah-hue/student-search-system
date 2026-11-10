# ==============================================================================
# Project: Student Database Search System
# Purpose: Learning Python Loops and Optimization
# Author: Shahariar
# ==============================================================================

# Database of 96 students stored in variables:
print("---------- Welcome----------")
Liam="Liam- - 10- - 1"
Ava="Ava- - 10- - 2"
Elijah="Elijah- - 10- - 3"
Charlotte="Charlotte- - 10- - 4"
William="William- - 10- - 5"
Sophia="Sophia- - 10- - 6"
James="James- - 10- - 7"
Amelia="Amelia- - 10- - 8"
Benjamin="Benjamin- - 10- - 9"
Isabella="Isabella- - 10- - 10"
Lucas="Lucas- - 10- - 11"
Mia="Mia- - 10- - 12"
Henry="Henry- - 10- - 13"
Evelyn="Evelyn- - 10- - 14"
Alexander="Alexander- - 10- - 15"
Harper="Harper- - 10- - 16"
Mason="Mason- - 10- - 17"
Camila="Camila- - 10- - 18"
Michael="Michael- - 10- - 19"
Gianna="Gianna- - 10- - 20"
Ethan="Ethan- - 10- - 21"
Abigail="Abigail- - 10- - 22"
Daniel="Daniel- - 10- - 23"
Luna="Luna- - 10- - 24"
Jacob="Jacob- - 10- - 25"
Ella="Ella- - 10- - 26"
Logan="Logan- - 10- - 27"
Elizabeth="Elizabeth- - 10- - 28"
Jackson="Jackson- - 10- - 29"
Sofia="Sofia- - 10- - 30"
Levi="Levi- - 10- - 31"
Avery="Avery- - 10- - 32"
Sebastian="Sebastian- - 10- - 33"
Scarlett="Scarlett- - 10- - 34"
Mateo="Mateo- - 10- - 35"
Emily="Emily- - 10- - 36"
Jack="Jack- - 10- - 37"
Aria="Aria- - 10- - 38"
Owen="Owen- - 10- - 39"
Penelope="Penelope- - 10- - 40"
John="John- - 10- - 41"
Chloe="Chloe- - 10- - 42"
Wyatt="Wyatt- - 10- - 43"
Layla="Layla- - 10- - 44"
Luke="Luke- - 10- - 45"
Milani="Milani- - 10- - 46"
Julian="Julian- - 10- - 47"
Nora="Nora- - 10- - 48"
Hazel="Hazel- - 10- - 49"
Grayson="Grayson- - 10- - 50"
Lily="Lily- - 10- - 51"
Isaac="Isaac- - 10- - 52"
Elena="Elena- - 10- - 53"
Jayden="Jayden- - 10- - 54"
Naomi="Naomi- - 10- - 55"
Gabriel="Gabriel- - 10- - 56"
Eliana="Eliana- - 10- - 57"
Anthony="Anthony- - 10- - 58"
Dylan="Dylan- - 10- - 59"
Violet="Violet- - 10- - 60"
Leo="Leo- - 10- - 61"
Madison="Madison- - 10- - 62"
Lincoln="Lincoln- - 10- - 63"
Stella="Stella- - 10- - 64"
Jaxon="Jaxon- - 10- - 65"
Maya="Maya- - 10- - 66"
Christopher="Christopher- - 10- - 67"
Zoe="Zoe- - 10- - 68"
Josiah="Josiah- - 10- - 69"
Ivy="Ivy- - 10- - 70"
Andrew="Andrew- - 10- - 71"
Grace="Grace- - 10- - 72"
Thomas="Thomas- - 10- - 73"
Isla="Isla- - 10- - 74"
Joshua="Joshua- - 10- - 75"
Kinsley="Kinsley- - 10- - 76"
Ezra="Ezra- - 10- - 77"
Aurora="Aurora- - 10- - 78"
David="David- - 10- - 79"
Bella="Bella- - 10- - 80"
Matthew="Matthew- - 10- - 81"
Nova="Nova- - 10- - 82"
Samuel="Samuel- - 10- - 83"
Paisley="Paisley- - 10- - 84"
Joseph="Joseph- - 10- - 85"
Audrey="Audrey- - 10- - 86"
Caleb="Caleb- - 10- - 87"
Willow="Willow- - 10- - 88"
Nathan="Nathan- - 10- - 89"
Clara="Clara- - 10- - 90"
Ryan="Ryan- - 10- - 91"
Aaliyah="Aaliyah- - 10- - 92"
Adrian="Adrian- - 10- - 93"
Cora="Cora- - 10- - 94"
Alice="Alice- - 10- - 95"
Bob="Bob- - 10- - 96"

# Master Tuple used to save memory space:

s_names= (
    Liam, Ava, Elijah, Charlotte, William, Sophia, James, 
    Amelia, Benjamin, Isabella, Lucas, Mia, Henry, Evelyn, 
    Alexander, Harper, Mason, Camila, Michael, Gianna, Ethan, 
    Abigail, Daniel, Luna, Jacob, Ella, Logan, Elizabeth, 
    Jackson, Sofia, Levi, Avery, Sebastian, Scarlett, Mateo, 
    Emily, Jack, Aria, Owen, Penelope, John, Chloe, Wyatt, 
    Layla, Luke, Milani, Julian, Nora, Hazel, Grayson, Lily, 
    Isaac, Elena, Jayden, Naomi, Gabriel, Eliana, Anthony, 
    Dylan, Violet, Leo, Madison, Lincoln, Stella, Jaxon, 
    Maya, Christopher, Zoe, Josiah, Ivy, Andrew, Grace, 
    Thomas, Isla, Joshua, Kinsley, Ezra, Aurora, David, 
    Bella, Matthew, Nova, Samuel, Paisley, Joseph, Audrey, 
    Caleb, Willow, Nathan, Clara, Ryan, Aaliyah, Adrian, 
    Cora, Alice, Bob
)

# Take user input and clean it up:

a_1 = input("student Name's: ").strip().title()

# Flag variable to track search status:
found = False

# Print output table header:
print("NAME- - CLASS- - ROLL")

# Loop through the database to find the student:
for i in s_names:
    if a_1 in i:
        print(i) 
        found = True
        break     

# Handle case where student is not found:
if not found:
    print("Sorry, this student does not exist in our database.")
