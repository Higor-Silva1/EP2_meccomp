classdef Bar
    
    properties
        E       (1,1) {mustBeNumeric};
        A       (1,1) {mustBeNumeric};
        L       (1,1) {mustBeNumeric};
        pho     (1,1) {mustBeNumeric};
        I       (1,1) {mustBeNumeric};
        node1   (1,1) {mustBeNumeric};
        node2   (1,1) {mustBeNumeric};
        theta   (1,1) {mustBeNumeric};
    end
    
    methods
        function self = Bar(E, A, L, pho, I, node1, node2,theta)
        self.E = E;          %bar's elastic module
        self.A = A;          %bar's section area
        self.L = L;          %bar's size
        self.pho = pho;      %bar's density
        self.I = I;          %Inertia
        self.node1 = node1;  %first bar's node
        self.node2 = node2;
        self.theta = theta*pi/180;  %bar's angle to the horizontalvarargin)
        end
        
        function matrix_test = method1(self,inputArg)
            %METHOD1 Summary of this method goes here
            %   Detailed explanation goes here
            matrix_test = self.E + inputArg;
        end
    end
end

