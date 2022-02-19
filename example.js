/* import {Handlebars} from 'https://twitter.github.io/typeahead.js/js/handlebars.js'; */

require('https://twitter.github.io/typeahead.js/js/handlebars.js')

function say(nombre){
    console.log("hello, "+nombre+"!")
}

function renderisar(){
    var data = {EmisorNumeroDocumento: "jjjjxxxjjjj"}
    Handlebars.tpl("plan.html", {
        success: function(renderer){
            console.log("Rendered template:", renderer(data));
        },
        error: function(xhr, err){
            console.warn("Ooops, can't load template", err);
        }
    });
};
