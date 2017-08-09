/**
 * Created by jevin on 8/9/2017.
 */

(function () {
    'use strict';

    angular
        .module('thinkster.authentication', [
            'thinkster.authentication.controllers',
            'thinkster.authenctication.services'
        ]);

    angular
        .module('thinkster.authentication.controllers', []);

    angular
        .module('thinkster.authentication.services', ['ngCookies']);
})();