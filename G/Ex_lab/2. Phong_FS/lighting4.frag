#version 330 core

in vec3 N;
in vec3 P;

out vec4 fragColor;


//  Ka, Kd, Ks, S
uniform vec4 matAmbient;
uniform vec4 matDiffuse;
uniform vec4 matSpecular;
uniform float matShininess;


// pos. llum (eye space), Ia,  Id,  Is
uniform vec4 lightPosition;
uniform vec4 lightAmbient;
uniform vec4 lightDiffuse;
uniform vec4 lightSpecular;

vec4 Phong (vec3 N, vec3 L, vec3 V) {
  N = normalize (N);
  V = normalize (V);
  L = normalize (L);
  vec3 R = normalize (2*dot(N, L)*N-L);
  
  float auxR = max(0, dot(R, V));
  float auxN = max(0, dot(N, L));
  float lspec = 0; 
  if (auxN > 0) lspec = pow(auxR, matShininess); 
  
  vec4 f1 = matAmbient * lightAmbient;
  vec4 f2 = matDiffuse * lightDiffuse * auxN;
  vec4 f3 = matSpecular * lightSpecular * lspec;
  
  return f1 + f2 + f3;
}

void main()
{
    vec3 L = (lightPosition - vec4(P, 1.0)).xyz;
    vec3 V = - P;
    fragColor = Phong(N, L, V);
}
