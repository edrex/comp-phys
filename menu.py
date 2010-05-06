#!/usr/bin/python
from pend_solver import *
import cmd

class Prompt(cmd.Cmd):
    
    """Simple command processor for interacting with the solver. 
    See http://www.doughellmann.com/PyMOTW/cmd/index.html
    and http://docs.python.org/library/cmd.html
    """
    
    prompt = 'solver: '
    intro = 'A simple differential equation solver routine.'


    def do_vars(self, line):
        print "Variables:"
        for key,value in self.var.items():
            print key,'\t:\t',value
        print 'alg\t:\t',self.solver

    def do_solve(self, line):
        V=self.var        
        print "Running solver..."
        T,X,V = solve(x_0, v_0, accel_func)
    
    def do_algorithm(self, line):
        args = line.split()
        if len(args) == 2 and args[1] in algorithms.keys():
            algorithm = args[1]
        
    def complete_algorithm(self, text, line, begidx, endidx):
        print text, line
        if text:
            return (key for key in algorithms.keys() if key.startswith(text))
        else:
            return algorithms.keys()
                    
    def do_system(self, line):
        args = line.split()
        if len(args) == 2 and args[1] in algorithms.keys():
            alg = args[1]
        
    def do_quit(self, line):
        print "Hope you enjoyed the program!"
        return True

    def do_EOF(self, line):
        '''make ^D work to exit'''
        
        print "Hope you enjoyed the program!"
        return True

    def default(self, line):
        args = line.split()
        if len(args) == 2:
            if args[0] == 'solver':
                self.vars['solver'] = args[1]
            elif (args[0] in self.vars.keys()):
                self.vars[args[0]] = args[1]

    def completedefault(self, text, line, begidx, endidx):
        print endidx,'blah'
        return self.vars.keys()
        
if __name__ == '__main__':
    Prompt().cmdloop()
    
