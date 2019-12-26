function [ u ] = pd_controller(~, s, s_des, params)
%PD_CONTROLLER  PD controller for the height
%
%   s: 2x1 vector containing the current state [z; v_z]
%   s_des: 2x1 vector containing desired state [z; v_z]
%   params: robot parameters

syms err1 err2 err3 kp kv m real


m=params.mass
err1 = s_des(1)-s(1)
err2 = s_des(2)-s(2)
err3 = (err2^2)
kp = 100*err1
kv = 18*err2
s(1)
u = m.*(err3 + kp + kv + params.gravity)

% FILL IN YOUR CODE HERE



end

