/*
* @Author: Brian Cherinka
* @Date:   2016-05-31 14:20:07
* @Last Modified by:   Brian Cherinka
* @Last Modified time: 2016-06-19 21:33:21
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

        // Event Handlers - code that runs when specific events occur from the user
        //
        // Let's set a mouse click event to the button element on the Example page
        // This creates an event listener that says when this specific button
        // element is clicked (on-click), then call the method getRandomNumber, and
        // also pass the Example self into the method attached to the event.
        // http://api.jquery.com/on/
        // syntax: .on(eventtype, optional parameter to attach to event.data, function name)
        this.myrandom_button.on('click', this, this.getRandomNumber);
        // event handler to toggle the session variable when it is clicked
        this.changesess_button.on('click', this, this.setSessionVariable);

    }

    // Initialize the object
    Example.prototype.init = function() {
        // this.parametername is a public and global property.
        // Attaching it to this makes it accessible inside and outside object
        // "this" is similar to "self" from a Python class

        // you can set variables
        this.myname = 'example';
        // or div elements from your page
        this.myrandom_button = $('#randombutton'); // id of the button to get random numbers
        this.myrandom_output = $('#randomoutput'); // id of the div to place the output number
        this.randomform = $('#randomform'); // id of the random number form
        this.changesess_button = $('#changesession'); // id of the button to change the session variable
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
        // I optionally passed in the Example self which I recover here.
        // I do this so I can accesd Example methods/variables inside new events
        var _this = event.data;
        // the variable this is now mapped to the button element instead of the Example object

        // Recover the form parameters you need to send to the server
        // I want the inputs from the RandomNumber Form
        // serializeArray will collect all form elements and create an array of
        // Objects of the form {'name': elementname, 'value': elementvalue}
        // This requires your form elements to have the 'name' property specified
        var form = _this.randomform.serializeArray();

        // I am a JQuery Ajax Http POST request (https://api.jquery.com/jquery.post/)
        // Also called a JQuery Deferred Object
        // I am a unit of work to be completed later
        $.post(Flask.url_for('example_page.getrandom'), form, 'json')
            .done(function(data) {
                // I am a callback that runs when the back-end code is successful
                _this.checkStatus(data.result);
            })
            .fail(function(data) {
                // I am a callback that runs when the server or method crashes on the back-end
                // I catch uncaught errors from the backend
                _this.checkStatus(data.result);
            })
    };

    // Check the status of the results from the Button Callback
    Example.prototype.checkStatus = function checkStatus(result) {
        // Remove any prior classes that have been added to the output div
        this.myrandom_output.removeClass();
        if (result === undefined) {
            // Callback has Failed
            // Add the alert-danger class to the output div
            this.myrandom_output.addClass('alert alert-danger');
            // Add an error message to the html output
            this.myrandom_output.html('Error: Failed to retrieve number.  Please check for crashes!');
        } else if (result.status === -1) {
            // Callback was a success but something went wrong inside
            // Add the alert-danger class to the output div
            this.myrandom_output.addClass('alert alert-danger');
            // Add an error message to the html output
            this.myrandom_output.html(result.error);
        } else {
            // Callback was a success and status is good
            // Add the alert-success class to the output div
            this.myrandom_output.addClass('alert alert-success');
            // Add the number to the html output
            this.myrandom_output.html('Success: '+result.number);
        }
    };

    // Set the Flask session variable loadcat
    Example.prototype.setSessionVariable = function setSessionVariable(event) {
        var _this = event.data;
        // is the button active?
        var isactive = _this.changesess_button.hasClass('active');
        var form = {'isactive': isactive};
        console.log(form);
        $.post(Flask.url_for('example_page.changesession'), form, 'json')
            .done(function(data) {
                // I am a callback that runs when the back-end code is successful
                console.log('done');
                if (isactive) {
                 _this.changesess_button.button('reset');
                } else {
                 _this.changesess_button.button('complete');
                }
                window.reload();
            })
            .fail(function(data) {
                // I am a callback that runs when the server or method crashes on the back-end
                // I catch uncaught errors from the backend
                console.log('fail');
                //_this.checkStatus(data.result);
            })
    };

    return Example;
})();
