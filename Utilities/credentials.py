import random
import string

def firstName():
    names = (
        'Alexia','Alacia','Jordan','John','Andy','Joe','Caroline','Jennifer','Olivia','Anthony','Karen','Linda',
        'Emily','Sophia','Isabella','Mia','Charlotte','Amelia','Evelyn','Abigail','Harper','Ella',
        'Avery','Scarlett','Grace','Chloe','Camila','Penelope','Riley','Layla','Lillian','Nora',
        'Zoey','Mila','Aubrey','Hannah','Lily','Addison','Eleanor','Natalie','Luna','Savannah',
        'Brooklyn','Leah','Zoe','Stella','Hazel','Ellie','Paisley','Audrey','Skylar','Violet',
        'Claire','Bella','Aurora','Lucy','Anna','Samantha','Caroline','Genesis','Aaliyah','Kennedy',
        'Kinsley','Allison','Maya','Sarah','Madelyn','Adeline','Alexa','Ariana','Elena','Gabriella',
        'Naomi','Alice','Sadie','Hailey','Eva','Emilia','Autumn','Quinn','Nevaeh','Piper','Ruby',
        'Serenity','Willow','Everly','Cora','Kaylee','Lydia','Aubree','Arianna','Eliana','Peyton',
        'Melanie','Gianna','Isabelle','Julia','Valentina','Nova','Clara','Vivian','Reagan','Mackenzie',
        'Madeline','Brielle','Delilah','Isla','Rylee','Katherine','Sophie','Josephine','Ivy','Jade',
        "Bradly","Brad","Bradford"
    )
    return random.choice(names)

def lastName():
    names = (
        'Johnson','Smith','Williams','Thompson','Friday','Lynch','Baker','Stout','Scott','Tuesday','Perez','Lopez',
        'Brown','Jones','Garcia','Miller','Davis','Rodriguez','Martinez','Hernandez','Lopez','Gonzalez',
        'Wilson','Anderson','Thomas','Taylor','Moore','Jackson','Martin','Lee','Perez','Thompson',
        'White','Harris','Sanchez','Clark','Ramirez','Lewis','Robinson','Walker','Young','Allen',
        'King','Wright','Scott','Torres','Nguyen','Hill','Flores','Green','Adams','Nelson',
        'Baker','Hall','Rivera','Campbell','Mitchell','Carter','Roberts','Gomez','Phillips','Evans',
        'Turner','Diaz','Parker','Cruz','Edwards','Collins','Reyes','Stewart','Morris','Morales',
        'Murphy','Cook','Rogers','Gutierrez','Ortiz','Morgan','Cooper','Peterson','Bailey','Reed',
        'Kelly','Howard','Ramos','Kim','Cox','Ward','Richardson','Watson','Brooks','Chavez',
        'Wood','James','Bennett','Gray','Mendoza','Ruiz','Hughes','Price','Alvarez','Castillo',
        'Sanders','Patel','Myers','Long','Ross','Foster','Jimenez','Powell','Jenkins','Perry',
        'Russell','Sullivan','Bell','Coleman','Butler','Henderson','Barnes','Gonzales','Fisher','Vasquez',
        'Alpers'
    )
    return random.choice(names)

def password():
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    size = random.randint(12, 16)
    return ''.join(random.choice(chars) for _ in range(size))



