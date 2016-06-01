/*
* @Author: Brian Cherinka
* @Date:   2016-05-31 14:20:07
* @Last Modified by:   Brian Cherinka
* @Last Modified time: 2016-05-31 17:04:08
*/

// Example Javascript object.
// I am like a Python class but not really.  I can be instantiated.
//
// I am code that is purely client-side.  Once I'm loaded in the browser, it
// becomes my home.  I live there and do all the things to the front-end,
// or send commands back to the server asynchronously so you don't need to wait or
// reload the page.  Love me please.

// This enforces a strict javascript syntax format
'use strict';

var Example = (function() {

    // Constructor - I am called upon object instantiation
    function Example() {

        // in case constructor called without new
        if (false === (this instanceof Example)) {
            return new Example();
        }

        // Initialize any parameters or run methods.  These happen after the
        // object has been set up during construction
        this.init();

        // Event Handlers
        //
        // Let's set a click event to the button element on the Example page
        this.myrandom_button.on('click', this, this.getRandomNumber);

    }

    // Initialize the object
    Example.prototype.init = function() {
        // this.parametername is a public and global property.
        // Attaching it to this makes it accessible inside and outside object
        // "this" is similar to "self" from a Python class

        // you can set variables
        this.myname = 'example';
        // or div elements from your page
        this.myrandom_button = $('#randombutton');
        this.myrandom_output = $('#randomoutput');
        this.randomform = $('#randomform');
        // this is how you run functions within itself
        this.print();
    };

    // Javascript method.  Prototype means it's publicly available.
    // It also helps to map methods to unique namespaces.  If you loaded another
    // javascript object with a print function, your code won't get confused, as this
    // print is mapped to the Example object.
    Example.prototype.print = function print() {
        // This is how to print to the Developers Console in your browser
        console.log('I am a new Example Javascript object');
        // You can also try and catch things
        try {
            var newvariable = x;
        } catch (err) {
            // console.error captures the full traceback of your error
            console.error('I have caught an error: ', err);
        }
        // I can also make just a warning
        console.warn('You have been warned');
    };

    // A Private Javascript method.  This can only be used internally
    // within the Example object
    Example.myname = function myname() {
        console.log('My name is ', this.myname);
        console.log('No one else can see me from the outside!');
    };

    // Add two numbers together
    Example.prototype.add = function add(x, y) {
        var z = x + y;
        console.log('I am adding '+x+' and '+y+'!');
        return z;
    };

    // Get a random number from the server and display it
    // This method is an event handler, so the input is the event that is calling it
    // In this case, it is the button click event
    Example.prototype.getRandomNumber = function getRandomNumber(event) {
        var _this = event.data;
        console.log('randform', _this.randomform);
        var form = _this.randomform.serializeArray();
        console.log('form', form);

        // I am a JQuery Ajax Http POST request (https://api.jquery.com/jquery.post/)
        // Also called a JQuery Deferred Object
        // I am a unit of work to be completed later
        $.post(Flask.url_for('example_page.getrandom'), form, 'json')
            .done(function(data) {
                // I am a callback that runs when the back-end code is successful
                console.log('done');
                _this.myrandom_output.html(data.result.number);
            })
            .fail(function(data) {
                // I am a callback that runs when the server or method crashes on the back-end
            })
    };

    return Example;
})();
