#define trigPin 13  
#define echoPin 12

#define PIN_RED 2
#define PIN_YELLOW 3
#define PIN_GREEN 4

float duration, distance;  

void setup() {
  
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(PIN_RED, OUTPUT);
  pinMode(PIN_YELLOW, OUTPUT);
  pinMode(PIN_GREEN, OUTPUT);
  digitalWrite(PIN_RED, LOW);
  digitalWrite(PIN_YELLOW, LOW);
  digitalWrite(PIN_GREEN, LOW);

  Serial.begin(9600);

}

void loop() {
   digitalWrite(trigPin, LOW);  // Ensure the trigPin is LOW initially
  delayMicroseconds(2);        // Small delay
  digitalWrite(trigPin, HIGH); // Send a pulse
  delayMicroseconds(10);       // Pulse duration
  digitalWrite(trigPin, LOW);  // End pulse

  // Measure the time taken for the echo to return
  duration = pulseIn(echoPin, HIGH);  

  // Calculate the distance in centimeters
  distance = (duration * 0.0343) / 2;


  if(distance > 0 && distance <20){

    digitalWrite(PIN_RED,HIGH);
    digitalWrite(PIN_YELLOW, LOW);
    digitalWrite(PIN_GREEN, LOW);

  }
  else if(distance >= 20 && distance <50){

    digitalWrite(PIN_YELLOW, HIGH);
    digitalWrite(PIN_RED, LOW);
    digitalWrite(PIN_GREEN, LOW);

  }
  else{

    digitalWrite(PIN_GREEN, HIGH);
    digitalWrite(PIN_RED, LOW);
    digitalWrite(PIN_YELLOW, LOW);

  }
  
    // Print the distance to the serial monitor
    Serial.println(distance);



    delay(100);

}


