describe('hello', function() {
  it('gives me my personalized credentials', function() {
    cy.visit('https://hello-flask-example.herokuapp.com/credentials/view/Isaac');
    cy.get('body > p')
      .should('contain', 'credentials')
      .should('contain', 'Isaac');
  });
});
