## Tree Classification Telegram Bot

### What this is about

This is a tree classifier that has been deployed into telegram. It classifies the image to one of the 16 trees:

'Angsana',
 'Batoko Plum',
 'Broad-leafed Mahogany',
 'Casuarina',
 'Chengal Pasir',
 'Gelam',
 'Golden Penda',
 'Hankerchief Tree',
 'Leopard Tree',
 'Madagascar Almond',
 'Pink Mempat',
 'Rain Tree',
 'Red Lip',
 'Sea Almond',
 'Sea Gutta',
 'Trumpet Tree'

These are the 16 most common trees in Singapore, according to Nparks (https://www.nparks.gov.sg/treessg/learn/know-our-trees)

### How to use 

Add the bot - tree-detector-bot (it does not detect trees, just classifies)

Upload an image to the bot

The bot would output a tree name based on the 16 above.

Obviously, if you gave it a non-tree image, it will give you rubbish.

### How to run the app

Make sure you have a heroku account and have created a heroku app on which to run the bot and have created your bot.
Also - make sure to have your configs done, especially your heroku app name and the telegram bot token. This would be saved on your config.ini or on heroku (see settings)


add the files - 
> git add <the files>

git commit every file - 

> git commit -m 'YOUR MESSAGE'

push to heroku - 

> git push heroku master

if all goes well, you can interface with your bot. 

### Data

The data are in the repository. The model was trained on very little data as you can see. This is due to not being able to get much pictures. The model can be improved with more data. 

The data was also augmented to improve the dataset size, although this did not improve the mdoel that much. 
