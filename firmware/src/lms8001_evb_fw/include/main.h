#ifndef MAIN_H_
#define MAIN_H_

/* Exported defines---------------------------------------------------------- */


/* Exported Enums---- ------------------------------------------------------- */
enum {LED_MODE_OFF, LED_MODE_ON, LED_MODE_WINK, LED_MODE_BLINK1, LED_MODE_BLINK2};


/* Exported functions ------------------------------------------------------- */
/**	Function to control LED mode. */
void Set_LED_mode (unsigned char LED, unsigned char mode);

#endif
