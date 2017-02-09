angular.module('myModule', ['schemaForm', 'ngSanitize'])
    .controller('FormController', function($scope) {

        //These pull from separate schema, form and model files included in page head
        $scope.schema = gentooSchema;
        $scope.form = gentooForm;
        $scope.model = gentooModel;

        $scope.onSubmit = function(form) {
        // First we broadcast an event so all fields validate themselves
        $scope.$broadcast('schemaFormValidate');

        // VALIDATE FORM
        if (form.$valid) {

            jsonForm = JSON.stringify($scope.model, undefined, 2);
            console.log(jsonForm);

        }
    }
});
