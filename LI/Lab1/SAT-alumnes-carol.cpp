#include <iostream>
#include <stdlib.h>
#include <algorithm>
#include <vector>
using namespace std;

//CAROLINA MIDDEL SORIA

#define UNDEF -1
#define TRUE 1
#define FALSE 0

uint numVars;
uint numClauses;
vector<vector<int> > clauses;
vector<int> model;
vector<int> modelStack;
uint indexOfNextLitToPropagate;
uint decisionLevel;

vector <double> cont_act;
vector < vector <int>> lit_positius;
vector < vector <int>> lit_negatius;

int decisions;
int conflictes;
int num_div;


void ini_vecs () {
    cont_act = vector <double> (numVars+1, 0.);
    lit_negatius = vector < vector <int>> (numVars+1);
    lit_positius = vector < vector <int>> (numVars+1);
    decisions = 0;
    conflictes = 0;    
}


void readClauses( ){
  // Skip comments
  char c = cin.get();
  while (c == 'c') {
    while (c != '\n') c = cin.get();
    c = cin.get();
  }  
  // Read "cnf numVars numClauses"
  string aux;
  cin >> aux >> numVars >> numClauses;
  ini_vecs();
  num_div = numClauses/8;
  clauses.resize(numClauses);  
  // Read clauses
  for (uint i = 0; i < numClauses; ++i) {
    int lit;
    while (cin >> lit and lit != 0) {
        clauses[i].push_back(lit);
        if (lit > 0) {
            lit_positius[lit].push_back(i);
            ++cont_act[lit];
        }
        else {
            lit_negatius[-lit].push_back(i);
            ++cont_act[-lit];
        }
    }
  }    
}



int currentValueInModel(int lit){
  if (lit >= 0) return model[lit];
  else {
    if (model[-lit] == UNDEF) return UNDEF;
    else return 1 - model[-lit];
  }
}


void setLiteralToTrue(int lit){
  modelStack.push_back(lit);
  if (lit > 0) model[lit] = TRUE;
  else model[-lit] = FALSE;		
}


void comp_act (int num) {
    ++conflictes;
    if (conflictes%num_div == 0) {
        for (uint i =1; i<numVars; ++i) {
            cont_act[i] /= 2.;
        }
    }
    for (uint i=0; i<clauses[num].size(); ++i) {
        int lit = abs(clauses[num][i]);
        ++cont_act[lit];
    }
}


//-------------------------------------------------------------



//separar per vectors de literals positius i neg, per trobar més ràpid
// contador d'activitats, decisions i conflictes
bool propagateGivesConflict ( ) {
  while ( indexOfNextLitToPropagate < modelStack.size() ) {
      bool positiu = true;
      int lit = modelStack[indexOfNextLitToPropagate];
      if (lit <= 0) {
          lit = -lit;
          positiu = false;
      }
      int posicions;
      if (positiu) posicions = lit_negatius[lit].size();
      else posicions = lit_positius[lit].size();
      ++indexOfNextLitToPropagate;
      
      for (int i = 0; i < posicions; ++i) {
        bool someLitTrue = false;
        int numUndefs = 0;
        int lastLitUndef = 0;
        int act = lit_negatius[lit][i];
        if (!positiu) act = lit_positius[lit][i];
        
        for (uint k = 0; not someLitTrue and k < clauses[act].size(); ++k){
            int val = currentValueInModel(clauses[act][k]);
            if (val == TRUE) someLitTrue = true;
            else if (val == UNDEF) {
                ++numUndefs;
                lastLitUndef = clauses [act][k];
            }
        }
        if (not someLitTrue and numUndefs == 0) {
            comp_act(act);
            return true; // conflict! all lits false
        }
        else if (not someLitTrue and numUndefs == 1) setLiteralToTrue(lastLitUndef);	
    }    
  }
  return false;
}



void backtrack(){
  uint i = modelStack.size() -1;
  int lit = 0;
  while (modelStack[i] != 0){ // 0 is the DL mark
    lit = modelStack[i];
    model[abs(lit)] = UNDEF;
    modelStack.pop_back();
    --i;
  }
  // at this point, lit is the last decision
  modelStack.pop_back(); // remove the DL mark
  --decisionLevel;
  indexOfNextLitToPropagate = modelStack.size();
  setLiteralToTrue(-lit);  // reverse last decision
}


// Heuristic for finding the next decision literal:
int getNextDecisionLiteral(){
    int n = 0;
    int lit = 0;
    
  for (uint i = 1; i <= numVars; ++i) {// stupid heuristic:
    if (model[i] == UNDEF and cont_act[i] > n){
        n = cont_act[i];
        lit = i;
    }
  }
  ++decisions;
  return lit; // reurns lit when all literals are defined
}

//-------------------------------------------------------------


void checkmodel(){
  for (uint i = 0; i < numClauses; ++i){
    bool someTrue = false;
    for (uint j = 0; not someTrue and j < clauses[i].size(); ++j)
      someTrue = (currentValueInModel(clauses[i][j]) == TRUE);
    if (not someTrue) {
      cout << "Error in model, clause is not satisfied:";
      for (uint j = 0; j < clauses[i].size(); ++j) cout << clauses[i][j] << " ";
      cout << endl;
      exit(1);
    }
  }  
}

int main(){ 
  readClauses(); // reads numVars, numClauses and clauses
  model.resize(numVars+1,UNDEF);
  indexOfNextLitToPropagate = 0;  
  decisionLevel = 0;
  
  // Take care of initial unit clauses, if any
  for (uint i = 0; i < numClauses; ++i)
    if (clauses[i].size() == 1) {
      int lit = clauses[i][0];
      int val = currentValueInModel(lit);
      if (val == FALSE) {
          cout << "UNSATISFIABLE" << endl;
          cout << "c " << decisions << " decisions" << endl;
          return 10;
      }
      else if (val == UNDEF) setLiteralToTrue(lit);
    }
  
  // DPLL algorithm
  while (true) {
    while ( propagateGivesConflict() ) {
      if ( decisionLevel == 0) {
          cout << "UNSATISFIABLE" << endl;
          cout << "c " << decisions << " decisions" << endl;
          return 10; 
      }
      backtrack();
    }
    int decisionLit = getNextDecisionLiteral();
    if (decisionLit == 0) { 
        checkmodel(); 
        cout << "SATISFIABLE" << endl;
        cout << "c " << decisions << " decisions" << endl;
        return 20; 
    }
        
    // start new decision level:
    modelStack.push_back(0);  // push mark indicating new DL
    ++indexOfNextLitToPropagate;
    ++decisionLevel;
    setLiteralToTrue(decisionLit);    // now push decisionLit on top of the mark
  }
}  
