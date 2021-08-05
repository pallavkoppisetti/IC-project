% MinimumHammingDistanceDecoder() takes in input arguments y (the decoder
% input) and the code C. It returns the estimate codeword from C (decoder output)
% such that the Hamming distance between the estimate and y is the minimum possible
% from all codewords present in C.

function estimate = MinimumHammingDistanceDecoder(y,C)

min_distance = length(y)+1;

% Array to store the indexes of all the codewords in C that satisfy the
% minimum Hamming distance condition.
min_index = [];

% Array to store the Hamming distance of all the codewords in C, and y.
distance = zeros(1,height(C));

for nn = 1:height(C)
    for mm = 1:length(y)
        % If the bits are not equal, increment the Hamming distance count
        % of that codeword.
        if C(nn,mm) ~= y(mm)
            distance(nn) = distance(nn)+1;
        end
    end
    
    % If the Hamming distance of the codeword in the current iteration is
    % less than the minimum Hamming distance of all previous iterations,
    % then this will be the new minimum.
    if distance(nn) < min_distance
        min_distance = distance(nn);
        % The codeword in the current iteration is the new estimate if the
        % above if condition is satisfied.
        min_index = nn;
        
        % If the Hamming distance of the codeword in the current iteration is
        % equal to the minimum Hamming distance of all previous iterations,
        % then this codeword is also a valid estimate, along with the
        % previously found estimate. So, we add it's index to the array
    elseif distance(nn) == min_distance
        min_index = [min_index nn];
    end
end

% Decoder randomly selects a codeword from all such codewords satisfying
% the minimum Hamming distance condition as the estimate, and the output of
% the decoder.
estimate = C(min_index(randi(length(min_index))),:);
end