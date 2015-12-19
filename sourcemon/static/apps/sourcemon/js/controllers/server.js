(function(module) {
    var ServerController = function(server, dataService, $location) {
        var self = this;
        self.data = server;
        self.players = self.data.players;

        self.getDuration = function(dur){
            return Math.round(dur / 60);
        };

        self.remove = function(){
            var res = dataService.removeServer(self.data.id);
            res.success(function(data, status, headers, config) {
                $location.path('/');
            });
            res.error(function(data, status, headers, config) {
                alert( "failure message: " + JSON.stringify({data: data}));
            });
        };
    };

    module.controller('ServerController', ServerController);
}(angular.module('sourcemon')));
