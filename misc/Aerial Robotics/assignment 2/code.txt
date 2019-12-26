function [ u1, u2 ] = controller(~, state, des_state, params)
%CONTROLLER  Controller for the planar quadrotor
%
%   state: The current state of the robot with the following fields:
%   state.pos = [y; z], state.vel = [y_dot; z_dot], state.rot = [phi],
%   state.omega = [phi_dot]
%
%   des_state: The desired states are:
%   des_state.pos = [y; z], des_state.vel = [y_dot; z_dot], des_state.acc =
%   [y_ddot; z_ddot]
%
%   params: robot parameters

%   Using these current and desired states, you have to compute the desired
%   controls
syms cphi cphi2 cphi3 phic1 phic2 phic3 ginvert real


cphi = (-1.0/params.gravity)*(des_state.acc(1)+5*(des_state.vel(1)-state.vel(1))+20*(des_state.pos(1)-state.pos(1)))
cphi2= 0
cphi3= 0


u1 = params.mass.*(params.gravity + des_state.acc(2)+20.*(des_state.vel(2)-state.vel(2))+80.*(des_state.pos(2)-state.pos(2)));
u2 = params.Ixx*(cphi3+10*(cphi2-state.omega(1))+1000*(cphi(end)-state.rot(1)));

% FILL IN YOUR CODE HERE

end

