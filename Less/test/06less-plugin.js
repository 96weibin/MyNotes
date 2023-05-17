module.exports =  {
    install: function(less, pluginManager, functions){
        functions.add('pi', function(){
            return Math.PI;
        })

        functions.add('theme', function(){
            // let theme = localStorage.getItem('theme');
            theme = 'dark';
            return theme;
        })
    }
}