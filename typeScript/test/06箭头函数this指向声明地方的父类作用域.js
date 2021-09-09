var deck = {
    suits: ['hearts', 'spades', 'clubs', 'diamonds'],
    cards: Array(52),
    createCardPicker: function () {
        var that = this;
        return function () {
            var pickedCard = Math.floor(Math.random() * 52);
            var pickedSuit = Math.floor(pickedCard / 13);
            return {
                suit: that.suits[pickedSuit],
                card: pickedCard % 13
            };
        };
    }
};
var cardPicker = deck.createCardPicker(); //this   deck  谁调用 this指向谁 
var pickedCard = cardPicker(); //{suit:Err,card:num}
console.log('card :' + pickedCard.card + 'of' + pickedCard.suit);
