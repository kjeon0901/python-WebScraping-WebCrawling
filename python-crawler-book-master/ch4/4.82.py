var = 'egoism,as a form of hedonism, is the doctirne which holds that we ought each of us to pursue our own greates gappiness as our ultimate end. the doctrine will , of course, admit that sometimes the best means to the end will be to give pleasure to others; we shall, for instance, by so doing , procure for ourselves the pleasure of sympathy, of freedom from interference, and of self- esteem; and these pleasures, which we may procure by something aiming directly at the happiness of other persons , may be greater than any we could otherwise get.'

space_ps = var.split(' ')

char_frequency = {}

for char in space_ps:
    char_frequency.setdefault(char, 0)
    char_frequency[char] += 1
print(char_frequency)
