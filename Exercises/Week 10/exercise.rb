arduino = {
    'uno' => {
        'microcontroller' => 'ATmega328',
        'digitalPins' => 14,
        'analogPins' => 6,
        'timers' => [0,1,2]
    },
    'nano' => {
        'microcontroller' => 'ATmega328',
        'digitalPins' => 14,
        'analogPins' => 8,
        'timers' => [0,1,2]
    },
    'mega' => {
        'microcontroller' => 'ATmega2560',
        'digitalPins' => 54,
        'analogPins' => 16,
        'timers' => [0, 1, 2, 3, 4, 5]
    }
}

puts arduino['uno'].inspect
puts arduino['nano'].inspect
puts arduino['mega'].inspect