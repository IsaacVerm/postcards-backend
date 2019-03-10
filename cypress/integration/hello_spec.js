describe('Postcards', function() {
  it('shows a welcome message', function() {
    cy.visit('https://hello-flask-example.herokuapp.com/me');
    cy.get('p').should.contain('Welcome to the postcards site, Isaac');
  });
});
