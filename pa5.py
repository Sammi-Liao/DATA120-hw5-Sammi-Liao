# Problem 1: Bisection Method
def bisection_root(function, lower_bond, upper_bond):
    '''Perform Bisection root'''
    if function(lower_bond) * function(upper_bond) > 0:
        raise ValueError('We cannot expect to find a root between \
                         two points on the same side of the 𝑥-axis')
    if abs(function(lower_bond)) < 1e-6:
        return lower_bond
    if abs(function(upper_bond)) < 1e-6:
        return upper_bond

    new_x = (lower_bond + upper_bond)/2
    new_y = function(new_x)
    if abs(new_y) < 1e-6:
        return new_x
    if function(lower_bond) * new_y > 0:
        return bisection_root(function, new_x, upper_bond)
    return bisection_root(function, lower_bond, new_x)


# Problem 2: Dictionary Filter
def dict_filter(function, diction):
    '''Takes in a function and a dictionary and produces a new dictionary
    where a given key and value remain associated with each other in the
    new dictionary, if and only if the function returns True when called
    with the key and the value.'''
    new_dict = {}
    for name, value in diction.items():
        if function(name, value):
            new_dict[name] = value
    return new_dict


# Problem 3: Tree Map
class KVTree:
    '''A KVTree'''
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)


samplekv = KVTree("us", 4.6)
pa = KVTree("pa", 1.9)
samplekv.add_child(pa)
pa.add_child(KVTree("Pittsburgh", 0.3))
pa.add_child(KVTree("Philadelphia", 1.6))
il = KVTree("il", 2.7)
samplekv.add_child(il)
il.add_child(KVTree("Chicago", 2.7))

def treemap(function, tree):
    '''Takes in a function and one of these trees and
    modifies the tree according to the function'''
    (tree.key, tree.value) = function(tree.key, tree.value)
    for child in tree.children:
        treemap(function, child)


# Problem 4: Trees Modeling Decisions
class DTree:
    def __init__(self, variable, threshold, lessequal, greater, outcome):
        if ((variable is not None and threshold is not None and
             lessequal is not None and greater is not None) and
            (outcome is None)) or ((variable is None and
                                    threshold is None and
                                    lessequal is None and
                                    greater is None) and
                                    (outcome is not None)):
            self.variable = variable
            self.threshold = threshold
            self.lessequal = lessequal
            self.greater = greater
            self.outcome = outcome
        else:
            raise ValueError("The input values are invalid")

    def tuple_atleast(self):
        '''Analyzes the tree and determines how many entries
        there need to be in the tuple'''
        if self.lessequal is None and self.greater is None:
            if self.variable is None:
                return 0
            return self.variable + 1
        elif self.lessequal:
            return max(self.variable + 1, self.lessequal.tuple_atleast())
        elif self.greater:
            return max(self.variable + 1, self.greater.tuple_atleast())

    def find_outcome(self, tup):
        '''Takes in a tuple with observations and navigates through the tree
        to provide the outcome that matches (like “walk”)'''
        if self.lessequal is None and self.greater is None:
            return self.outcome
        elif tup[self.variable] > self.threshold:
            return self.greater.find_outcome(tup)
        else:
            return self.lessequal.find_outcome(tup)

    def no_repeats(self):
        '''Analyzes the tree and returns True if and only if there
        are not “repeats”, False otherwise'''
        return self.helper(set())

    def helper(self, variable_set):
        if self.variable in variable_set:
            return False
        if self.lessequal is None and self.greater is None:
            return True
        variable_set.add(self.variable)
        return (self.lessequal.helper(set(variable_set)) and
                self.greater.helper(set(variable_set)))
