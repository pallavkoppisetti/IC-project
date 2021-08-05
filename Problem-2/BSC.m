% BSC() simulates a binary symmetric channel. It takes in input arguments c
% and p where c is the codeword to be transmitted and p is the probablity
% of bit flip. It returns the received codeword y at the end of the binary
% symmetric channel.

function y = BSC(c,p)

% Initialising y as an empty string
y = blanks(length(c));

for nn = 1:length(c)
    
    % Randomly generating a number rand_num in the range (0,1)
    % using rand(). rand() returns a number from the uniform distribution
    % in the range (0,1). So, the probability of rand_num being less
    % than or equal to p (p can take values in the range [0,1]) is
    % equivalent to simulating an event with probability p.
    rand_num = rand();
    if rand_num <= p % Bit-flip
        if c(nn) == '1'
            y(nn) = '0';
        else
            y(nn) = '1';
        end
    else % No bit-flip
        y(nn) = c(nn);
    end
end
end