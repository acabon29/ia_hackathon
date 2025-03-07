const int trigPin = 11; // Trigger
const int echoPin = 12; // Echo
long duree; // durée de l'echo 
int distance; // distance 

void setup() {
   pinMode(trigPin, OUTPUT); // Configuration du port du Trigger comme une SORTIE 
   pinMode(echoPin, INPUT); // Configuration du port de l'Echo comme une ENTREE 
   Serial.begin(9600); // Démarrage de la communication série 
} 

void loop() { 
   // Émission d'un signal de durée 10 microsecondes 
   digitalWrite(trigPin, LOW); 
   delayMicroseconds(5); 
   digitalWrite(trigPin, HIGH);
   delayMicroseconds(10); 
   digitalWrite(trigPin, LOW); 

   // Écoute de l'écho 
   duree = pulseIn(echoPin, HIGH); 

   // Calcul de la distance 
   distance = duree*0.034/2; 

   // Affichage de la distance dans le Moniteur Série 
   Serial.print("Distance : "); 
   Serial.print(distance); 
   Serial.println("cm"); 
}