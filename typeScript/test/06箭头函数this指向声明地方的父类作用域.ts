let deck = {
    suits : ['hearts', 'spades', 'clubs', 'diamonds'],
    cards:Array(52),
    createCardPicker:function(){
        let that = this;
        return function(){
            let pickedCard = Math.floor(Math.random() * 52);
            let pickedSuit = Math.floor(pickedCard / 13);
            return {
                suit:that.suits[pickedSuit],
                card:pickedCard % 13
            };
        }
    }
}

let cardPicker = deck.createCardPicker();   //this   deck  谁调用 this指向谁 
let pickedCard = cardPicker();     //{suit:Err,card:num}
console.log('card :' + pickedCard.card + 'of' + pickedCard.suit)