#include <Arduino.h>
#include <SPI.h>
#include "Adafruit_BLE.h"
#include "Adafruit_BluefruitLE_SPI.h"
#include "Adafruit_BluefruitLE_UART.h"

#include "BluefruitConfig.h"

#if SOFTWARE_SERIAL_AVAILABLE
  #include <SoftwareSerial.h>
#endif
//pins 5 and 6 are free
int inPin = 6;   // input pin for pushbutton
int pinStat = 0; // variable for reading pin status
int led = 5;     // receive data led
int led_send = 3;// send data led
//const int ledP = 13;      // led connected to digital pin 13, not used at the moment
const int knockSensor = A0; // the piezo is connected to analog pin 0
const int threshold = 500;  // threshold value to decide when the detected sound is a knock or not
int sensorReading = 0;      // variable to store the value read from the sensor pin
int ledState = LOW;         // variable used to store the last LED status, to toggle the light

    #define FACTORYRESET_ENABLE         1
    #define MINIMUM_FIRMWARE_VERSION    "0.6.6"
    #define MODE_LED_BEHAVIOUR          "MODE"
/*=========================================================================*/

/* ...hardware SPI, using SCK/MOSI/MISO hardware SPI pins and then user selected CS/IRQ/RST */
Adafruit_BluefruitLE_SPI ble(BLUEFRUIT_SPI_CS, BLUEFRUIT_SPI_IRQ, BLUEFRUIT_SPI_RST);

// A small helper
void error(const __FlashStringHelper*err) {
  Serial.println(err);
  while (1);
}

/**************************************************************************/
/*!
    @brief  Sets up the HW an the BLE module (this function is called
            automatically on startup)
*/
/**************************************************************************/
void setup(void)
{
  pinMode(led_send, OUTPUT);
  pinMode(led, OUTPUT);
  pinMode(inPin, INPUT); //declare pushbutton as input
  //while (!Serial);  // required for Flora & Micro
  delay(500);

  Serial.begin(115200);
  Serial.println(F("ECE 4900 Demo"));
  Serial.println(F("---------------------------------------"));

  /* Initialise the module */
  Serial.print(F("Initialising the Bluefruit LE module: "));

  if ( !ble.begin(VERBOSE_MODE) )
  {
    error(F("Couldn't find Bluefruit, make sure it's in CoMmanD mode & check wiring?"));
  }
  Serial.println( F("OK!") );

  if ( FACTORYRESET_ENABLE )
  {
    /* Perform a factory reset to make sure everything is in a known state */
    Serial.println(F("Performing a factory reset: "));
    if ( ! ble.factoryReset() ){
      error(F("Couldn't factory reset"));
    }
  }

  /* Disable command echo from Bluefruit */
  ble.echo(false);

  Serial.println("Requesting Bluefruit info:");
  /* Print Bluefruit information */
  ble.info();

  Serial.println(F("Please use Adafruit Bluefruit LE app to connect in UART mode"));
  Serial.println(F("Then Enter characters to send to Bluefruit"));
  Serial.println();

  ble.verbose(false);  // debug info is a little annoying after this point!

  /* Wait for connection */
  while (! ble.isConnected()) {
      delay(500);
  }

  // LED Activity command is only supported from 0.6.6
  if ( ble.isVersionAtLeast(MINIMUM_FIRMWARE_VERSION) )
  {
    // Change Mode LED Activity
    Serial.println(F("******************************"));
    Serial.println(F("Change LED activity to " MODE_LED_BEHAVIOUR));
    ble.sendCommandCheckOK("AT+HWModeLED=" MODE_LED_BEHAVIOUR);
    Serial.println(F("******************************"));
  }
}

/**************************************************************************/
/*!
    @brief  Constantly poll for new command or response data
*/
/**************************************************************************/
void loop(void)
{
  // Check for user input
  char inputs[BUFSIZE+1];
*/
 // read the sensor and store it in the variable sensorReading:
  sensorReading = analogRead(knockSensor);
  if (sensorReading >= threshold) {
    ble.print("AT+BLEUARTTX=");
    ble.println(9);
    
    // check response stastus
    if ( ble.waitForOK() ) {
      digitalWrite(led_send, HIGH);
      delay(500);
      digitalWrite(led_send, LOW);
    }
    else {
      Serial.println(F("Failed to send?"));
    }
  }
  
 //send ascii 8 to the connected device
  pinStat = digitalRead(inPin); //read input pin
  if (pinStat == HIGH){    //if the button is pressed
  //for(i=0;i<5;i++){
    ble.print("AT+BLEUARTTX=");
    ble.println(8);
    
    // check response stastus
    if ( ble.waitForOK() ) {
      digitalWrite(led_send, HIGH);
      delay(500);
      digitalWrite(led_send, LOW);
    }
    else {
      Serial.println(F("Failed to send?"));
    }
  pinStat = 0;
  //delay(500);//delay to allow person to take their finger off the button
 }

 
  // Check for incoming characters from Bluefruit
  ble.println("AT+BLEUARTRX");
  ble.readline();
  if (strcmp(ble.buffer, "OK") == 0) {
    // no data
    return;
  }
  
  // Some data was found, its in the buffer
  Serial.print(F("[Recv] ")); Serial.println(ble.buffer);
  
  if ( ble.waitForOK() ){
    digitalWrite(led, HIGH);
    delay(1000);
    digitalWrite(led, LOW);
  }
  //pinStat = 0;
  
}

/**************************************************************************/
/*!
    @brief  Checks for user input (via the Serial Monitor)
*/
/**************************************************************************/
bool getUserInput(char buffer[], uint8_t maxSize)
{
  // timeout in 100 milliseconds
  TimeoutTimer timeout(100);

  memset(buffer, 0, maxSize);
  while( (!Serial.available()) && !timeout.expired() ) { delay(1); }

  if ( timeout.expired() ) return false;

  delay(2);
  uint8_t count=0;
  do
  {
    count += Serial.readBytes(buffer+count, maxSize);
    delay(2);
  } while( (count < maxSize) && (Serial.available()) );

  return true;
}
