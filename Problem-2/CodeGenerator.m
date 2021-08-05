% CodeGenerator() takes in input arguments num and n; and randomly
% generates a code C (where each codeword is a binary string of length n)
% of cardinality 'num' by randomly picking 'num' unique vectors from the
% binary vector space {0,1}^n.

function C = CodeGenerator(num, n)
rng('shuffle');

% Initializing the binary vector space {0,1}^n (in decimal format)
binvector_space = 0:2^n-1;
C_dec = zeros(num,1); % Set of codewords in decimal format

% Generating the code in decimal format
for nn = 1:num
    % Randomly pick a number from binvector_space and add it to C_dec.
    r = randi(length(binvector_space));
    C_dec(nn) = binvector_space(r);
    
    % To ensure that all codewords are unique, the codeword generated
    % in the above step is removed from binvector_space.
    if r == 1
        binvector_space = binvector_space(1,2:length(binvector_space));
    elseif r == length(binvector_space)
        binvector_space = binvector_space(1,1:length(binvector_space)-1);
    else
        binvector_space = [binvector_space(1,1:r-1) binvector_space(1,r+1:length(binvector_space))];
    end
end

% Converting the code in decimal format to binary (C is the code where
% each codeword is a binary string of length n).
C = dec2bin(C_dec,n);
end