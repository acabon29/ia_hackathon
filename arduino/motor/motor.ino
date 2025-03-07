// const int bouton = 2; // the button is connected to pin 2 of the Adruino board
const int relais_moteur = 2; // the relay is connected to pin 3 of the Adruino board
int etatBouton;
unsigned long currentMillis = 0;
const long interval = 500;

void setup()
{
  Serial.begin(9600);
  // pinMode(bouton, INPUT);
  pinMode(relais_moteur, OUTPUT);
}

void loop()
{

  // Check if data is received
  if (Serial.available() > 0)
  {
    char command = Serial.read(); // Read the received command

    if (command == 'R') {
      digitalWrite(relais_moteur, HIGH);
      // currentMillis = millis();
      delay(500);
      digitalWrite(relais_moteur, LOW);
      delay(500);
    }

    // other method (does not work) :
    // if (command == 'R') {
    //   digitalWrite(relais_moteur, HIGH);
    //   currentMillis = millis();
    // }
    // if (currentMillis != 0 && millis() - currentMillis > interval)
    // {
    //   digitalWrite(relais_moteur, LOW);
    //   currentMillis = 0;
    // }
    delay(10);
  }
}